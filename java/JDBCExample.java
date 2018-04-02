import java.sql.*;

public class JDBCExample {

  public static void main(String[] argv) {

	System.out.println("-------- MySQL JDBC Connection Testing ------------");

	try {
		Class.forName("com.mysql.jdbc.Driver");
	} catch (ClassNotFoundException e) {
		System.out.println("Where is your MySQL JDBC Driver?");
		e.printStackTrace();
		return;
	}

	System.out.println("MySQL JDBC Driver Registered!");
	Connection connection = null;

	try {
		 connection = DriverManager
		.getConnection("jdbc:mysql://localhost:3306/ebookshop?useSSL=false", "root", "123456");
		
		String strSelect = "select title, price, qty from books";
		System.out.println("The SQL query is: " + strSelect); // Echo For debugging
		System.out.println();

		Statement stmt = connection.createStatement();
		ResultSet rset = stmt.executeQuery(strSelect);

		// Step 4: Process the ResultSet by scrolling the cursor forward via next().
		//  For each row, retrieve the contents of the cells with getXxx(columnName).
		System.out.println("The records selected are:");
		int rowCount = 0;
		while(rset.next()) {   // Move the cursor to the next row, return false if no more row
            String title = rset.getString("title");
            double price = rset.getDouble("price");
            int    qty   = rset.getInt("qty");
            System.out.println(title + ", " + price + ", " + qty);
            ++rowCount;	
         }
         System.out.println("Total number of records = " + rowCount);

	} catch (SQLException e) {
		System.out.println("Connection Failed! Check output console");
		e.printStackTrace();
		return;
	}

	if (connection != null) {
		System.out.println("You made it, take control your database now!");
	} else {
		System.out.println("Failed to make connection!");
	}
  }
}
