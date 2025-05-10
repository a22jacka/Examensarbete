// run with: k6 run wildfire_post.js --console-output=filename.csv

import { sleep } from 'k6';
import http from 'k6/http';
//import { uuidv4 } from 'https://jslib.k6.io/k6-utils/1.4.0/index.js';
import { uuidv4 } from './libs/uuidv4.js'
import { open } from 'k6/experimental/fs';
import csv from 'k6/experimental/csv';
import { vu } from 'k6/execution';

const vus = 10;
const iterPerVu = 100;

export const options = {
    vus: vus,
    iterations: 2000, //vus * iterPerVu,
    //duration: '2m'
};

const file = await open("../USFS_FireData.csv");
const parser = new csv.Parser(file, { asObjects: true });

// the fields that should be switched to numbers. 
// Just doing a loop doesn't work since not all fields that can be numbers should be numbers
const convertToNumber = ["x", "y", "objectid", "fireyear", "sofirenum", "localfirenum", "securityid", "totalacres", "datasource", "latdd83", "longdd83", "dbsourceid", "accuracy"];

export function setup() {
    http.del("http://localhost:8080/cleardb");
    console.log(`id,status,startTime,stopTime,durationJS,durationK6,vus,bodyLength`);
}

export default async function () {
    const { done, value } = await parser.next();
    if (done) {
        throw new Error("EOF");
    }

    // seperate data object since the numbers aren't converting correctly
    const data = { id: uuidv4() }

    // a zero-width space someho get's in from the file, so this is needed to remove that 
    value.x = value["﻿x"];
    delete value["﻿x"];

    // convert number attributes to numbers instead of strings
    for (const [key, val] of Object.entries(value)) {
        if (convertToNumber.includes(key)) {
            data[key] = parseFloat(val);
        } else {
            data[key] = val;
        }
    }
    const constData = {
        "id": uuidv4(),
        "accuracy": 24000,
        "perimexists": "N",
        "firename": "Battlement Mesa Reservoir",
        "securityid": 215,
        "sizeclass": "A",
        "datasource": 24,
        "owneragency": "USFS",
        "longdd83": -107.93556,
        "firerptqc": "Yes",
        "dbsourcedate": "2024/09/24 04:01:15+00",
        "cn": "",
        "uniqfireid": "2016-COWRF-000452",
        "localfirenum": 452,
        "comments": " ",
        "fireoutdatetime": "2016/08/12 11:20:01+00",
        "x": -107.93555556,
        "revdate": "2023/03/29 11:10:59+00",
        "complexname": "",
        "sofirenum": 18,
        "unitidowner": "COWRF",
        "pointtype": "General",
        "dbsourceid": 215,
        "fireyear": 2016,
        "firetypecategory": "WF",
        "shape": "",
        "y": 39.37277778,
        "fireoccurid": "A2454D64-EBB7-4895-81BC-9782B3D1391E",
        "discoverydatetime": "2016/08/07 00:00:01+00",
        "statcause": "Camping",
        "protectionagency": "USFS",
        "latdd83": 39.37278,
        "globalid": "{ACE77CF8-1281-4A81-BE3D-4D55669CB134}",
        "unitidprotect": "COWRF",
        "objectid": 231055010,
        "totalacres": 0.1

    };
    const startTime = Date.now();
    const response = http.post("http://localhost:8080/wildfires/addentry", JSON.stringify(constData), {
        headers: { "Content-Type": "application/json" },
    });
    const stopTime = Date.now();
    if (response.status !== 200) {
        //console.log(response);
    }
    const duration = stopTime - startTime;

    console.log(`${data.id},${response.status},${startTime},${stopTime},${duration},${response.timings.duration},${vus},${JSON.stringify(constData).length}`);

    //sleep(0.5);
}