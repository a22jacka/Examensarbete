// run with: k6 run wildfire_get.js --console-output=filename.csv

import http from 'k6/http';
import { sleep } from 'k6';

import { uuidv4, randomIntBetween } from 'https://jslib.k6.io/k6-utils/1.4.0/index.js';

const vus = 10;
const iterPerVu = 2000 / vus;

export const options = {
    vus: vus,
    iterations: iterPerVu * vus,
    //executor: 'per-vu-iterations',
    //duration: '2m'
};

export function setup() {
    console.log(`testId,status,startTime,endTime,durationJS,durationK6,vus,limit,offset`);
}

export default function () {
    const testId = uuidv4();

    // based on how much data is supposed to be recieved, 1 entry returned = ~900B
    // limits used:
    //        13 =   10kB
    //        127 =  100kB
    //        1300 = 1MB
    const limit = 13;
    // number of entries in database, set manually
    const dbEntries = 10000;
    const offset = randomIntBetween(1, dbEntries - limit);

    const startTime = Date.now();
    const response = http.get(`http://localhost:8080/wildfires?limit=${limit}&offset=${offset}`);
    const endTime = Date.now();

    const duration = endTime - startTime;
    console.log(`${testId},${response.status},${startTime},${endTime},${duration},${response.timings.duration},${vus},${limit},${offset}`);

    sleep(0.5)
}