export default (activityData:any) => {
        const activity: string = activityData['activity'];
        const activityType: string = activityData['type'];
        const htmlString: string = "<head> <link rel='stylesheet' href='https://fonts.googleapis.com/css?family=Sofia'><head>"+
        "<h1 style='color:red'> Hello Dude !!! </title>  <h1> <br>"+
        "<body style='background-color:powderblue;font-family:Sofia'> Your activity : "+activity + "<br>" + 
        "Activity Type : "+activityType +"</body>";
        return  htmlString;
}
