package main

import (
	"database/sql"
	"net/http"

	_ "github.com/go-sql-driver/mysql"
	"github.com/labstack/echo/v4"
)

var db *sql.DB

func insertDbData(data WildFireEntry) {

}

func insertFireData() {

}

func getDbData(limit, offset int) {

}

func getFireData() {

}

func main() {
	// echo setup
	e := echo.New()
	e.GET("/", func(c echo.Context) error {
		return c.String(http.StatusOK, "Hello, World!")
	})

	// database setup
	var err error
	db, err = sql.Open("mysql", "root:exjobb@tcp(172.17.0.1:3306)/wildfire")
	if err != nil {
		panic(err)
	}

	port := ":8080"
	e.Logger.Fatal(e.Start(port))
}
