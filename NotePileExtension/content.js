chrome.runtime.onMessage.addListener(
    (request, sender, sendResponse) => {
        if (request["message"] === "clicked_browser_action") {
            const url = window.location.href;
            const range = window.getSelection().getRangeAt(0);
            const selectionContents = range.cloneContents();
            let img_arr = [];
            if (selectionContents.querySelector) {
                img_arr = Array.prototype.slice.call(selectionContents.querySelectorAll("img"));
                //img_arr = img_arr.map(el => ({height: el.height, width: el.width, src: el.src}));
                img_arr = img_arr.map(el => ({src: el.src}));
            }
            let text = ''
            if (window.getSelection().toString())
                text = "<p>" + window.getSelection().toString() + "</p>"
            const payload = { text: text, src: url, images: img_arr };
            sendResponse({content: JSON.stringify(payload)});
        }
    }
);
