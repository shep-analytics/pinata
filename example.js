const pinataSDK = require('@pinata/sdk');
const pinata = pinataSDK('key', 'priv');

const fs = require('fs');
const readableStreamForFile = fs.createReadStream('./black1.gif');
const options = {
    pinataMetadata: {
        name: blacktest,
        keyvalues: {
            stars: '4',
            blackhole: 'yes'
        }
    },
    pinataOptions: {
        cidVersion: 0
    }};
pinata.pinFileToIPFS(readableStreamForFile, options).then((result) => {
    //handle results here
    console.log(result);
}).catch((err) => {
    //handle error here
    console.log(err);
});
