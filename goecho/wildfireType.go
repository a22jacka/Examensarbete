package main

import "database/sql"

type WildFireEntry struct {
	Id                string
	X                 sql.NullFloat64
	Y                 sql.NullFloat64
	Objectid          sql.NullInt32
	Globalid          sql.NullString
	Fireoccureid      sql.NullString
	CN                sql.NullString
	Revdate           sql.NullString
	Firename          sql.NullString
	complexname       sql.NullString
	Fireyear          sql.NullInt32
	Uniquefireid      sql.NullString
	Sofirenum         sql.NullInt32
	Localfirenum      sql.NullInt32
	Securityid        sql.NullInt32
	Discoverydatetime sql.NullString
	Sizeclass         sql.NullString
	Totalacres        sql.NullFloat64
	Statcause         sql.NullString
	Comments          sql.NullString
	Datasource        sql.NullInt32
	Fireoutdatetime   sql.NullString
	Owneragency       sql.NullString
	Unitdowner        sql.NullString
	Protectionagency  sql.NullString
	Unitdprotect      sql.NullString
	Latdd83           sql.NullFloat64
	Longdd83          sql.NullFloat64
	Firetypecategory  sql.NullString
	Pointtype         sql.NullString
	Perimexists       sql.NullString
	Firerptqc         sql.NullString
	Dbsourceid        sql.NullInt32
	Dbsourcedate      sql.NullString
	Accuracy          sql.NullInt32
	Shape             sql.NullString
}

func ScanEntry(entry WildFireEntry, rows *sql.Rows) (WildFireEntry, error) {
	err := rows.Scan(
		&entry.Id,
		&entry.X,
		&entry.Y,
		&entry.Objectid,
		&entry.Globalid,
		&entry.Fireoccureid,
		&entry.CN,
		&entry.Revdate,
		&entry.Firename,
		&entry.complexname,
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
