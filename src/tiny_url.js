class TinyUrl {
	constructor(apiKey) {
		this.api = "https://tiny.cc/tiny/api/3"
		this.headers = {
			"authorization": apiKey,
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}
		this.apiKey = apiKey
	}

	async getAccountInfo() {
		const response = await fetch(
			`${this.api}/account`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async getShorteningUrls(
				longUrl,
				customHash = null,
				note = null,
				emailStats = null,
				tags = null,
				favorite = null,
				noStats = null) {
		let body = {
			urls: [{
				long_url: longUrl,
				email_stats: emailStats,
				favorite: favorite,
				no_stats: noStats
			}]
		}
		if (customHash) {
			body.urls.customHash = customHash
		}
		if (note) {
			body.urls.note = note
		}
		if (tags) {
			body.urls.tags = tags
		}
		const response = await fetch(
			`${this.api}/urls`, {
				method: "POST",
				body: JSON.stringify(body),
				headers: this.headers
			})
		return response.json()
	}

	async readUrls(offset = 0, limit = 10, search = null, orderBy = null) {
		let url = `${this.api}/urls?offset=${offset}&limit=${limit}`
		if (search) {
			url += `&search=${search}`
		}
		if (orderBy) {
			url += `&order_by=${orderBy}`
		}
		const response = await fetch(
			url, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async readSingleUrl(urlHash) {
		const response = await fetch(
			`${this.api}/urls/${urlHash}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}

	async deleteUrl(urlHash) {
		const response = await fetch(
			`${this.api}/urls/${urlHash}`, {
				method: "DELETE",
				headers: this.headers
			})
		return response.json()
	}

	async getUrlStats(urlHash) {
		const response = await fetch(
			`${this.api}/stats/${urlHash}`, {
				method: "GET",
				headers: this.headers
			})
		return response.json()
	}
 }

module.exports = {TinyUrl}
