// Setup Pinata SDK
const pinataSDK = require('@pinata/sdk')
const { pinFromFS } = pinataSDK('75f65d3ab9ee0f01b7ef', '015088d329750e235574fff5c4e0e3f4147de1c4d9b56c9ae7124d0987e6cfa0')

// Async Upload Function
const upload = async (filePath, name, variationData) => {
  try {
    return await pinFromFS('./black1.gif', { pinataMetadata: { name, keyvalues: variationData }, pinataOptions: { cidVersion: 0 } })
  } catch (err) {
    console.error(err)
    return err
  }
}

// Export Functions
exports.upload = upload

upload('./black1.gif', 'Test using new uploader', { color: 'red', eyes: 'Hazel' }).then(console.log).catch(console.error)