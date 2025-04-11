// run with: k6 run wildfire_post.js --console-output=filename.csv

import { sleep } from 'k6';
import http from 'k6/http';
import { uuidv4 } from 'https://jslib.k6.io/k6-utils/1.4.0/index.js';
import { open } from 'k6/experimental/fs';
import csv from 'k6/experimental/csv';
import { vu } from 'k6/execution';

const vus = 100;
const iterPerVu = 100;

export const options = {
    vus: vus,
    iterations: vus * iterPerVu,
    //duration: '2m'
};

const file = await open("../USFS_FireData.csv");
const parser = new csv.Parser(file, { asObjects: true });

// the fields that should be switched to numbers. 
// Just doing a loop doesn't work since not all fields that can be numbers should be numbers
const convertToNumber = ["x", "y", "objectid", "fireyear", "sofirenum", "localfirenum", "securityid", "totalacres", "datasource", "latdd83", "longdd83", "dbsourceid", "accuracy"];

export function setup() {
    console.log(`id,status,startTime,stopTime,durationJS,durationK6,vus`);
}

export default async function () {
    const { done, value } = await parser.next();
    if (done) {
        throw new Error("EOF");
    }

    // seperate data object since the numbers aren't converting correctly
    const id = uuidv4();
    const data = { id: id }

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

    const startTime = Date.now();
    const response = http.post("http://localhost:8080/wildfires/addentry", JSON.stringify({ id: id, ...data }), {
        headers: { "Content-Type": "application/json" },
    });
    const stopTime = Date.now();
    const duration = stopTime - startTime;

    console.log(`${id},${response.status},${startTime},${stopTime},${duration},${response.timings.duration},${vus}`);

    //sleep(1);
}