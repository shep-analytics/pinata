const pinataSDK = require('@pinata/sdk');
const pinata = pinataSDK('75f65d3ab9ee0f01b7ef', '015088d329750e235574fff5c4e0e3f4147de1c4d9b56c9ae7124d0987e6cfa0');
pinata.testAuthentication().then((result) => {
    //handle successful authentication here
    console.log(result);
}).catch((err) => {
    //handle error here
    console.log(err);
});