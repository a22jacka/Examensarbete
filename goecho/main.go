package main

import (
	"database/sql"
	"fmt"
	"net/http"
	"strconv"
	"time"

	_ "github.com/go-sql-driver/mysql"
	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

var db *sql.DB

func insertDbData(data WildFireEntry) (int64, error) {
	result, err := executeInsert(db, data)
	if err != nil {
		return 0, err
	}
	return result.LastInsertId()
}

func insertFireData(c echo.Context) error {
	var entry WildFireEntry
	var err error

	// binds the values from the request to the "entry" valuable
	if err = c.Bind(&entry); err != nil {
		return c.String(http.StatusBadRequest, "1 or more fields are invalid")
	}

	var id int64
	if id, err = insertDbData(entry); err != nil {
		return c.String(http.StatusServiceUnavailable, "Too many connections, try again later")
	}

	return c.String(http.StatusCreated, fmt.Sprintf("New Entry Added. ID: %d\n", id))
}

func getDbData(limit, offset int) ([]WildFireEntry, error) {
	// prepapre query and add the limit and offset if presenet
	query := fmt.Sprintf("SELECT * FROM WildfireEntry")
	if limit > 0 && offset > 0 {
		query = fmt.Sprintf("%s LIMIT %d OFFSET %d;", query, limit, offset)
	}

	rows, err := db.Query(fmt.Sprintf("%s;", query))
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var entries []WildFireEntry
	for rows.Next() {
		var entry WildFireEntry
		entry, err := ScanEntry(entry, rows)
		if err != nil {
			return nil, err
		}
		entries = append(entries, entry)
	}
	return entries, nil
}

func getFireData(c echo.Context) error {
	var err error

	// check that the parameters are present and valid numbers if present
	plimit := c.QueryParam("limit")
	limit := 0
	if plimit != "" {
		limit, err = strconv.Atoi(plimit)
		if err != nil {
			return c.String(http.StatusBadRequest, "Could not convert limit to int")
		}
	}
	poffset := c.QueryParam("offset")
	offset := 0
	if poffset != "" {
		offset, err = strconv.Atoi(poffset)
		if err != nil {
			return c.String(http.StatusBadRequest, "Could not convert offset to int")
		}
	}

	data, err := getDbData(limit, offset)
	if err != nil {
		panic(err)
	}

	return c.JSON(http.StatusOK, data)
}

func main() {
	// echo setup
	e := echo.New()
	e.Use(middleware.CORS())
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World!")
	})
	e.GET("/wildfires", getFireData)
	e.POST("/wildfires/addentry", insertFireData)

	// database setup
	var err error
	// local: "root:exjobb@/wildfire"
	// docker: "root:exjobb@tcp(172.17.0.1)/wildfire"
	connectionString := "root:exjobb@/wildfire"
	db, err = sql.Open("mysql", connectionString)
	if err != nil {
		panic(err)
	}

	db.SetMaxOpenConns(5000)
	db.SetMaxIdleConns(10000)
	db.SetConnMaxLifetime(time.Minute * 4)
	db.SetConnMaxIdleTime(time.Minute)

	port := ":8080"
	e.Logger.Fatal(e.Start(port))
}
