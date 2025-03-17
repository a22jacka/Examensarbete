package main

import (
	"database/sql"
)

type WildFireEntry struct {
	Id                string          `json:"id"`
	X                 sql.NullFloat64 `json:"x"`
	Y                 sql.NullFloat64 `json:"y"`
	Objectid          sql.NullInt32   `json:"objectid"`
	Globalid          sql.NullString  `json:"globalid"`
	Fireoccureid      sql.NullString  `json:"fireoccureid"`
	Cn                sql.NullString  `json:"cn"`
	Revdate           sql.NullString  `json:"revdate"`
	Firename          sql.NullString  `json:"firename"`
	Complexname       sql.NullString  `json:"complexname"`
	Fireyear          sql.NullInt32   `json:"fireyear"`
	Uniquefireid      sql.NullString  `json:"uniquefireid"`
	Sofirenum         sql.NullInt32   `json:"sofirenum"`
	Localfirenum      sql.NullInt32   `json:"localfirenum"`
	Securityid        sql.NullInt32   `json:"securityid"`
	Discoverydatetime sql.NullString  `json:"discoverydatetime"`
	Sizeclass         sql.NullString  `json:"sizeclass"`
	Totalacres        sql.NullFloat64 `json:"totalacres"`
	Statcause         sql.NullString  `json:"statcause"`
	Comments          sql.NullString  `json:"comments"`
	Datasource        sql.NullInt32   `json:"datasource"`
	Fireoutdatetime   sql.NullString  `json:"fireoutdatetime"`
	Owneragency       sql.NullString  `json:"owneragency"`
	Unitdowner        sql.NullString  `json:"unitdowner"`
	Protectionagency  sql.NullString  `json:"protectionagency"`
	Unitdprotect      sql.NullString  `json:"unitdprotect"`
	Latdd83           sql.NullFloat64 `json:"latdd83"`
	Longdd83          sql.NullFloat64 `json:"longdd83"`
	Firetypecategory  sql.NullString  `json:"firetypecategory"`
	Pointtype         sql.NullString  `json:"pointtype"`
	Perimexists       sql.NullString  `json:"perimexists"`
	Firerptqc         sql.NullString  `json:"firerptqc"`
	Dbsourceid        sql.NullInt32   `json:"dbsourceid"`
	Dbsourcedate      sql.NullString  `json:"dbsourcedate"`
	Accuracy          sql.NullInt32   `json:"accuracy"`
	Shape             sql.NullString  `json:"shape"`
}

func ScanEntry(entry WildFireEntry, rows *sql.Rows) (WildFireEntry, error) {
	err := rows.Scan(
		&entry.Id,
		&entry.X,
		&entry.Y,
		&entry.Objectid,
		&entry.Globalid,
		&entry.Fireoccureid,
		&entry.Cn,
		&entry.Revdate,
		&entry.Firename,
		&entry.Complexname,
		&entry.Fireyear,
		&entry.Uniquefireid,
		&entry.Sofirenum,
		&entry.Localfirenum,
		&entry.Securityid,
		&entry.Discoverydatetime,
		&entry.Sizeclass,
		&entry.Totalacres,
		&entry.Statcause,
		&entry.Comments,
		&entry.Datasource,
		&entry.Fireoutdatetime,
		&entry.Owneragency,
		&entry.Unitdowner,
		&entry.Protectionagency,
		&entry.Unitdprotect,
		&entry.Latdd83,
		&entry.Longdd83,
		&entry.Firetypecategory,
		&entry.Pointtype,
		&entry.Perimexists,
		&entry.Firerptqc,
		&entry.Dbsourceid,
		&entry.Dbsourcedate,
		&entry.Accuracy,
		&entry.Shape,
	)
	return entry, err
}

func executeInsert(db *sql.DB, data WildFireEntry) (sql.Result, error) {
	return db.Exec(
		"INSERT INTO WildfireEntry(ID, X, Y, OBJECTID, GLOBALID, FIREOCCURID, CN, REVDATE, FIRENAME, COMPLEXNAME, FIREYEAR, UNIQUEFIREID, SOFIRENUM, LOCALFIRENUM, SECURITYID, DISCOVERYDATETIME, SIZECLASS, TOTALACRES, STATCAUSE, COMMENTS, DATASOURCE, FIREOUTDATETIME, OWNERAGENCY, UNITDOWNER, PROTECTIONAGENCY, UNITDPROTECT, LATDD83, LONGDD83, FIRETYPECATEGORY, POINTTYPE, PERIMIEXISTS, FIRERPTQC, DBSOURCEID, DBSOURCEDATE, ACCURACY, SHAPE) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?);",
		data.Id, data.X, data.Y, data.Objectid, data.Globalid, data.Fireoccureid, data.Cn, data.Revdate, data.Firename, data.Complexname, data.Fireyear, data.Uniquefireid, data.Sofirenum, data.Localfirenum, data.Securityid, data.Discoverydatetime, data.Sizeclass, data.Totalacres, data.Statcause, data.Comments, data.Datasource, data.Fireoutdatetime, data.Owneragency, data.Unitdowner, data.Protectionagency, data.Unitdprotect, data.Latdd83, data.Longdd83, data.Firetypecategory, data.Pointtype, data.Perimexists, data.Firerptqc, data.Dbsourceid, data.Dbsourcedate, data.Accuracy, data.Shape)
}
