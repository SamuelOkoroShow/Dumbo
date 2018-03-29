var enabled = true;
chrome.webRequest.onBeforeRequest.addListener(
	function(details) {
		return {cancel: enabled };
	},
	{urls: youtube_blocked_domains},
	["blocking"]
);