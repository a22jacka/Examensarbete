// run with: k6 run wildfire_post.js --console-output=filename.csv

import http from 'k6/http';
import { uuidv4 } from 'https://jslib.k6.io/k6-utils/1.4.0/index.js';
import { open } from 'k6/experimental/fs';
import csv from 'k6/experimental/csv';
import { scenario } from 'k6/execution';

export const options = {
    //vus: 1,
    iterations: 1,
    //duration: '2m'
};

const file = await open("../USFS_FireData.csv");
const parser = new csv.Parser(file, { asObjects: true });

export default async function () {

    const { done, value } = await parser.next();
    if (done) {
        throw new Error("EOF");
    }

    const id = "c3";

    console.log(JSON.stringify({ ID: id, ...value }));

    const response = http.post("http://localhost:8080/wildfires/addentry", JSON.stringify({ ID: id, value }), {
        headers: { "Content-Type": "application/json" },
    });
}