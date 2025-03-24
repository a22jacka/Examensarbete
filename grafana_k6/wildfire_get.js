// run with: k6 run wildfire_get.js --console-output=filename.csv

import http from 'k6/http';

import { uuidv4 } from 'https://jslib.k6.io/k6-utils/1.4.0/index.js';

const vus = 1;
const iterPerVu = 1;
let limit, offset;

export const options = {
    vus: vus,
    iterations: vus * iterPerVu,
    //duration: '2m'
};

export function setup() {
    console.log(`testId,status,startTime,endTime,duration,duration,vus,limit,offset`);
}

export default function () {
    const testId = uuidv4();
    const startTime = Date.now();

    const response = http.get("http://localhost:8080/wildfires");

    const endTime = Date.now();
    const duration = endTime - startTime;
    console.log(`${testId},${response.status},${startTime},${endTime},${duration},${response.timings.duration},${vus},${limit},${offset}`);
    console.log(response);
}