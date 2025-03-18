package main

import (
	"database/sql"
)

// stored as pointers so that context.Bind doesn't fail
// sql.Null{Type} types exists, but can't interact with json
// Go also doesn't support null (nil) for regular types, they have null values instead ("" for string and 0 for int & float). Pointers can be null (nil)
type WildFireEntry struct {
	Id                string   `json:"id"`
	X                 *float64 `json:"x"`
	Y                 *float64 `json:"y"`
	Objectid          *int32   `json:"objectid"`
	Globalid          *string  `json:"globalid"`
	Fireoccureid      *string  `json:"fireoccureid"`
	Cn                *string  `json:"cn"`
	Revdate           *string  `json:"revdate"`
	Firename          *string  `json:"firename"`
	Complexname       *string  `json:"complexname"`
	Fireyear          *int32   `json:"fireyear"`
	Uniquefireid      *string  `json:"uniquefireid"`
	Sofirenum         *int32   `json:"sofirenum"`
	Localfirenum      *int32   `json:"localfirenum"`
	Securityid        *int32   `json:"securityid"`
	Discoverydatetime *string  `json:"discoverydatetime"`
	Sizeclass         *string  `json:"sizeclass"`
	Totalacres        *float64 `json:"totalacres"`
	Statcause         *string  `json:"statcause"`
	Comments          *string  `json:"comments"`
	Datasource        *int32   `json:"datasource"`
	Fireoutdatetime   *string  `json:"fireoutdatetime"`
	Owneragency       *string  `json:"owneragency"`
	Unitdowner        *string  `json:"unitdowner"`
	Protectionagency  *string  `json:"protectionagency"`
	Unitdprotect      *string  `json:"unitdprotect"`
	Latdd83           *float64 `json:"latdd83"`
	Longdd83          *float64 `json:"longdd83"`
	Firetypecategory  *string  `json:"firetypecategory"`
	Pointtype         *string  `json:"pointtype"`
	Perimexists       *string  `json:"perimexists"`
	Firerptqc         *string  `json:"firerptqc"`
	Dbsourceid        *int32   `json:"dbsourceid"`
	Dbsourcedate      *string  `json:"dbsourcedate"`
	Accuracy          *int32   `json:"accuracy"`
	Shape             *string  `json:"shape"`
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
