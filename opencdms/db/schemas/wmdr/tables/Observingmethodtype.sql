/* ---------------------------------------------------- */
/*  Generated by Enterprise Architect Version 15.2 		*/
/*  Created On : 04-May-2022 21:43:57 				*/
/*  DBMS       : PostgreSQL 						*/
/* ---------------------------------------------------- */

/* Drop Tables */

DROP TABLE IF EXISTS "Observingmethodtype" CASCADE
;

/* Create Tables */

CREATE TABLE "Observingmethodtype"
(
	"ObservingmethodtypeID" varchar NOT NULL
)
;

/* Create Primary Keys, Indexes, Uniques, Checks */

ALTER TABLE "Observingmethodtype" ADD CONSTRAINT "PK_Observingmethodtype"
	PRIMARY KEY ("ObservingmethodtypeID")
;

/* Create Table Comments, Sequences for Autonumber Columns */

COMMENT ON TABLE "Observingmethodtype"
	IS '5-02 Measurement/observing method type'
;