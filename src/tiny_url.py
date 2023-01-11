import requests
	
class TinyURL:
	def __init__(self, api_key: str) -> None:
		self.api = "https://tiny.cc/tiny/api/3"
		self.headers = {
			"authorization": api_key,
			"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.114 Safari/537.36"
		}
		self.api_key = api_key


	def get_account_info(self) -> dict:
		return requests.get(
			f"{self.api}/account",
			headers=self.headers).json()

	def get_shortening_urls(
			self,
			long_url: str,
			custom_hash: str = None,
			note: str = None,
			email_stats: bool = False,
			tags: list[str] = None,
			favorite: bool = False,
			no_stats: bool = True) -> dict:
		data = {
			"urls": [{
				"long_url": long_url,
				"email_stats": email_stats,
				"favorite": favorite,
				"no_stats": no_stats
			}]
		}
		if custom_hash:
			data["urls"]["custom_hash"] = custom_hash
		if note:
			data["urls"]["note"] = note
		if tags:
			data["urls"]["tags"]
		return requests.post(
			f"{self.api}/urls",
			data=data,
			headers=self.headers).json()

	def read_urls(
			self,
			offset: int = 0,
			limit: int = 10,
			search: str = None,
			order_by: str = None) -> dict:
		url = f"{self.api}/urls?offset={offset}&limit={limit}"
		if search:
			url += f"&search={search}"
		if order_by:
			url += f"&order_by={order_by}"
		return requests.get(
			url, headers=self.headers).json()

	def read_single_url(
			self,
			url_hash: str) -> dict:
		return requests.get(
			f"{self.api}/urls/{url_hash}",
			headers=self.headers).json()

	def edit_single_url(
			self,
			url_hash: str,
			long_url: str = None,
			custom_hash: str = None,
			note: str = None,
			email_stats: bool = False,
			tags: list[str] = None,
			favorite: bool = False,
			no_stats: bool = True) -> dict:
		data = {
			"urls": [{
				"email_stats": email_stats,
				"favorite": favorite,
				"no_stats": no_stats
			}]
		}
		if long_url:
			data["urls"]["long_url"] = long_url
		if custom_hash:
			data["urls"]["custom_hash"] = custom_hash
		if note:
			data["urls"]["note"] = note
		if tags:
			data["urls"]["tags"]
		return requests.patch(
			f"{self.api}/urls/{url_hash}",
			data=data,
			headers=self.headers).json()

	def delete_url(
			self,
			url_hash: str) -> dict:
		return requests.delete(
			f"{self.api}/urls/{url_hash}",
			headers=self.headers).json()

	def get_url_stats(
			self,
			url_hash: str) -> dict:
		return requests.get(
			f"{self.api}/stats/{url_hash}",
			headers=self.headers).json()
