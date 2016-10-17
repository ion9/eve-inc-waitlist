'use strict';
if (!getMetaData){
	var getMetaData = function (name) {
		return $('meta[name="'+name+'"]').attr('content');
	};
}
var eventSource;
var errorCount = 0;
function handleSSEError(event) {
	event.target.close();
	errorCount++;
	if (errorCount < 2) { // our first error reconnect this instant
		connectSSE();
	} else if (errorCount >= 2 && errorCount <= 5) {  // 2-5 errors, try reconnect after 1s
		setTimeout(connectSSE, 1000);
	} else { // > 5 errors try reconnect after 10s
		setTimeout(connectSSE, 10000);
	}
	event.target.close();
}

function handleSSEOpen(event) {
	if (errorCount > 1) {
		// refresh the page using json, to pull ALL the date, we might have missed sth
		refreshWl();
	}
	errorCount = 0; // reset error counter
}

function connectSSE() {
	eventSource = getSSE();
}

function fitAddedListener(event) {
	var data = JSON.parse(event.data);
	addFitToDom(data.listId, data.entryId, data.fit, data.isQueue, data.userId);
}

function entryAddedListener(event) {
	var data = JSON.parse(event.data);
	addNewEntry(data.listId, data.entry, data.groupId, data.isQueue);
}

function fitRemovedListener(event) {
	var data = JSON.parse(event.data);
	removeFitFromDom(data.listId, data.entryId, data.fitId);
}

function entryRemovedListener(event) {
	var data = JSON.parse(event.data);
	removeEntryFromDom(data.listId, data.entryId);
}

function gongListener(event) {
	if(gongEnabled()) {
		playGong();
	}
}

function missedInviteListener(event) {
	var data = JSON.parse(event.data);
	updateMissedInvite(data.userId);
}

function noSSE() {
	displayMessage('We have had to disable <strong>features</strong> please consider upgrading your<a href="http://caniuse.com/#feat=eventsource"> browser', 'danger');
	//setInterval(refreshWl, 30000);
}

function getSSE() {
	var sse = new EventSource(getMetaData('api-sse')+"?events="+encodeURIComponent("waitlistUpdates,gong")+"&groupId="+encodeURIComponent(getMetaData("wl-group-id")));
	sse.onerror = handleSSEError;
	sse.onopen = handleSSEOpen;
	
	sse.addEventListener("fit-added", fitAddedListener);
	sse.addEventListener("fit-removed", fitRemovedListener);
	
	sse.addEventListener("entry-added", entryAddedListener);
	sse.addEventListener("entry-removed", entryRemovedListener);

	sse.addEventListener("invite-send", gongListener);
	sse.addEventListener("invite-missed", missedInviteListener);
	
	return sse;
}

function wlsse() {
    if (!!window.EventSource) {
        connectSSE();
        refreshWl();
    } else {
        noSSE();
        refreshWl();
    }
}

document.addEventListener('DOMContentLoaded', wlsse);