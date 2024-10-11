# tiny_url.js
Web-API for [tiny.cc](https://tiny.cc) service to shorten urls

## Example
```JavaScript
async function main() {
	const { TinyUrl } = require("./tiny_url.js")
	const tinyUrl = new TinyUrl()
	const accountInfo = await tinyUrl.getAccountInfo()
  console.log(accountInfo)
}

main()
```
