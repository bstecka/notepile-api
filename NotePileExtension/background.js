function postData(url = '', data = {}) {
        return fetch(url, {
            method: 'POST',
            mode: 'cors',
            cache: 'no-cache',
            credentials: 'include',
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
            },
            redirect: 'follow',
            referrer: 'no-referrer',
            body: data.content,
        })
        .then(response => response.json());
    }

chrome.browserAction.onClicked.addListener((tab) => {
  chrome.tabs.query({active: true, currentWindow: true}, (tabs) => {
    const activeTab = tabs[0];
    chrome.tabs.sendMessage(activeTab.id, {"message": "clicked_browser_action"},
     (response) => {
        console.log(response["content"]);
        const content = response["content"];
        postData('http://localhost:8000/notes/', {content: response["content"]})
        .then((data) => {console.log(JSON.stringify(data))})
        .catch(error => console.error(error));
    });
  });
});

