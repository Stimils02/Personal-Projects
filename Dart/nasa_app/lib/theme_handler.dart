import 'package:flutter/material.dart';

// IconData iconLight = Icons.wb_sunny;
// IconData iconDark = Icons.nights_stay;

// ThemeData lightTheme = ThemeData(
//   primarySwatch: Colors.blue,
//   brightness: Brightness.light,
// );

// ThemeData darkTheme = ThemeData(
//   primarySwatch: Colors.red,
//   brightness: Brightness.dark,
// );
class ThemeModel extends ChangeNotifier {
  ThemeData currentTheme = ThemeData.light();
  bool isDarkTheme = false;
  Color backgroundColor = Colors.white;
  Color textColor = Colors.black;

  void switchMode() {
    isDarkTheme = !isDarkTheme;
    // isDarkTheme = isDarkTheme ? false : true;
    currentTheme = currentTheme == ThemeData.light()
        ? ThemeData.dark()
        : ThemeData.light();
    backgroundColor = isDarkTheme ? Colors.black : Colors.white;
    textColor = isDarkTheme ? Colors.white : Colors.black;
    notifyListeners();
  }
}
