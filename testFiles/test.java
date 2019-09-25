package Server;

import java.sql.*;

public class DataBase {
    String driver = "com.mysql.cj.jdbc.Driver";
    String url = "jdbc:mysql://localhost:3306/MoChat";
    String user = "root";
    String passwd = "woaidaitao";
    Connection connection;

    public DataBase() {
        try {
            Class.forName(driver);
            connection = DriverManager.getConnection(url, user, passwd);
            Main.outputMessage("数据库初始化完毕");
        } catch (ClassNotFoundException e) {
            System.out.println("加载MySQL驱动失败！");
        } catch (SQLException e) {
            System.out.println(e.getMessage());
        }
    }

    public String search(String targetTable, String condition, String target) {
        String res;
        try {
            Statement statement = connection.createStatement();
            ResultSet result = statement.executeQuery("SELECT * FROM " + targetTable + " WHERE (" + condition + ");");
            result.next();
            res = result.getString(target);
            statement.close();
            if (!res.equals("")) {
                return res;
            } else {
                System.out.println("Search null");
                return null;
            }
        } catch (SQLException e) {
            System.out.println("Search ERROR:" + e.getMessage());
            return null;
        }
    }

    public boolean set(String targetTable, String targetList, String value, String condition) {
        try {
            Statement statement = connection.createStatement();
            int result = statement.executeUpdate("UPDATE " + targetTable + " SET `" + targetList + "` = '" + value + "' WHERE (" + condition + ");");
            statement.close();
            if (result == 1) {
                return true;
            } else {
                return false;
            }
        } catch (SQLException e) {
            System.out.println("Set ERROR:" + e.getMessage());
            return false;
        }
    }
}
