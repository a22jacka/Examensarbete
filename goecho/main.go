package main

import (
	"database/sql"
	"fmt"
	"net/http"
	"strconv"

	_ "github.com/go-sql-driver/mysql"
	"github.com/labstack/echo/v4"
)

var db *sql.DB

func insertDbData(data WildFireEntry) {

}

func insertFireData(c echo.Context) error {
	return c.String(200, "ng :(")
}

func getDbData(limit, offset int) ([]WildFireEntry, error) {
	// prepapre query and add the limit and offset if presenet
	query := fmt.Sprintf("SELECT * FROM WildfireEntry;")
	if limit > 0 && offset > 0 {
		query = fmt.Sprintf("%s LIMIT %d OFFSET %d;", query, limit, offset)
	}

	rows, err := db.Query(query)
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
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World!")
	})
	e.GET("/wildfires", getFireData)
	e.POST("/wildfires/addentry", insertFireData)

	// database setup
	var err error
	// add "tcp(172.17.0.1)" when running for docker, remove for local
	db, err = sql.Open("mysql", "root:exjobb@tcp(172.17.0.1)/wildfire")
	if err != nil {
		panic(err)
	}

	port := ":8080"
	e.Logger.Fatal(e.Start(port))
}
