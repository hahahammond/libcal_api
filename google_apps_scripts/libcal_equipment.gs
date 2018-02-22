
// Writes LibCal equipment bookings in your system for the current date to a Google Spreadsheet


// Make request 
function run() {
  var url = 'https://api2.libcal.com/1.1/equipment/bookings?formAnswers=1';
  var response = UrlFetchApp.fetch(url, {
    headers: {
      'Authorization': 'Bearer ' + getLibCalToken(),
      'method': 'post'
    }
  });
  getJSON(response);
}

// Get LibCal OAuth token
var CLIENT_ID = '[ENTER CLIENT ID HERE]';
var CLIENT_SECRET = '[ENTER CLIENT SECRET HERE]';

function getLibCalToken() {  
  Logger.log('You are a member of Google Groups.');
  var tokenUrl = "https://api2.libcal.com/1.1/oauth/token";  
  var tokenCredential = Utilities.base64EncodeWebSafe(CLIENT_ID + ":" + CLIENT_SECRET);  
  //  Obtain a bearer token with HTTP POST request  
  var tokenOptions = {  
    headers : {  
      Authorization: "Basic " + tokenCredential,  
      "Content-Type": "application/x-www-form-urlencoded;charset=UTF-8"  
    },  
    method: "post",  
    payload: "grant_type=client_credentials"  
  };  
  var responseToken = UrlFetchApp.fetch(tokenUrl, tokenOptions);  
  var parsedToken = JSON.parse(responseToken);  
  var token = parsedToken.access_token;  
  Logger.log(responseToken);
  Logger.log(token);
  return token;
}  
  
// Get JSON  
function getJSON(response) {
  var json = JSON.parse(response.getContentText());
  Logger.log(json);
  //var my_json = JSON.stringify(result, null, 2);
  writeJSONtoSheet(json)
}

// Print data to sheet
function writeJSONtoSheet(json) {
  var ss = SpreadsheetApp.getActiveSpreadsheet();
  var sheets = ss.getSheets();
  var sheet = ss.getActiveSheet();

  var rows = [],
      data;
  

  for (i = 0; i < json.length; i++) {
    data = json[i];

    // Entity names (listed below) will vary based on what's included on your form. Adjust accordingly.
    rows.push([data.bookId,data.email,data.lastName,data.firstName,data.status,data.fromDate,data.toDate,data.lid,data.cid,data.eid,data.q2048,data.q2049,data.q2050,data.q2053,data.q2057,data.q2058,data.q2060,data.q2061,data.q2062,data.q2063]);
  }

// The number of entities (20 in this case) will vary based on what's included on your form. Adjust accordingly.
  dataRange = sheet.getRange(getFirstEmptyRowByColumnArray(), 1, rows.length, 20); 
  dataRange.setValues(rows);

}

// Find first empty row in sheet
function getFirstEmptyRowByColumnArray() {
  var spr = SpreadsheetApp.getActiveSpreadsheet();
  var column = spr.getRange('A:A');
  var values = column.getValues(); // get all data in one call
  var ct = 0;
  while ( values[ct] && values[ct][0] != "" ) {
    ct++;
  }
  return (ct+1);
}
  
  