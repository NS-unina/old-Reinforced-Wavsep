<%@ page language="java" contentType="text/html; charset=ISO-8859-1"
    pageEncoding="ISO-8859-1"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=ISO-8859-1">
<title>Case 3 - RXSS  exploitable Javascript and single quotes injection into a script block.</title>
</head>
<body>

<%
    try {
	  	String in = request.getParameter("in"); 
     		out.println("<script>var f = { date: '', week: '1', bad: '"+ in + "', phase: '2',};</script>");
	  	out.flush();
    } catch (Exception e) {
        out.println("Exception details: " + e);
    }
%>

Hello!<BR> 
This test demonstrates exploitable Injection due to unsafe handling of single quotes inside of a Javascript block.
</body>
</html>
