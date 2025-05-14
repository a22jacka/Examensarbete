import http from 'k6/http';
//import { uuidv4, randomIntBetween } from 'https://jslib.k6.io/k6-utils/1.4.0/index.js';
import { uuidv4 } from './libs/uuidv4.js'
import { open } from 'k6/experimental/fs';
import csv from 'k6/experimental/csv';

// iterations = number of entries in database
export const options = {
    iterations: 10000
}

const file = await open("../USFS_FireData.csv");
const parser = new csv.Parser(file, { asObjects: true });

// the fields that should be switched to numbers. 
// Just doing a loop doesn't work since not all fields that can be numbers should be numbers
const convertToNumber = ["x", "y", "objectid", "fireyear", "sofirenum", "localfirenum", "securityid", "totalacres", "datasource", "latdd83", "longdd83", "dbsourceid", "accuracy"];

export function setup() {
    http.del("http://localhost:8080/cleardb");
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

    const response = http.post("http://localhost:8080/wildfires/addentry", JSON.stringify({ id: id, ...data }), {
        headers: { "Content-Type": "application/json" },
    });
    if (response.status !== 201) {
        console.log(data);
        console.log(response.status_text)
    }
}