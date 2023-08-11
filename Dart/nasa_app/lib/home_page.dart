import 'package:flutter/material.dart';
import 'package:nasa_app/Settings_Page.dart';
import 'package:nasa_app/about_page.dart';
import 'package:nasa_app/theme_handler.dart';
import 'package:provider/provider.dart';

class HomePage extends StatelessWidget {
  const HomePage({super.key});

  @override
  Widget build(BuildContext context) {
    ThemeModel model = Provider.of<ThemeModel>(context);
    return Scaffold(
      backgroundColor: model.backgroundColor,
      appBar: AppBar(
        elevation: 0.0,
        backgroundColor: model.backgroundColor,
        title: Text(
          "You have entered Mission Control",
          style: TextStyle(color: model.textColor),
        ),
        centerTitle: true,
        actions: [
          IconButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const SettingsPage()),
              );
            },
            icon: Icon(
              Icons.settings,
              color: model.textColor,
            ),
          ),
          IconButton(
            onPressed: () {
              Navigator.push(
                context,
                MaterialPageRoute(builder: (context) => const AboutPage()),
              );
            },
            icon: Icon(
              Icons.question_mark,
              color: model.textColor,
            ),
          )
        ],
      ),
      body: Container(
        decoration: const BoxDecoration(
          image: DecorationImage(
            image: AssetImage('images/planets.jpg'),
          ),
        ),
      ),
    );
  }
}



// ThemeData darkTheme = ThemeData(
//   primarySwatch: Colors.amber,
//   brightness: Brightness.dark,
// );

// class HomePage extends StatelessWidget {
//   const HomePage({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return Center(
//       child: ElevatedButton(
//         onPressed: () {
//           Navigator.of(context).push(MaterialPageRoute(builder: (BuildContext context){
//             return const LearnFlutterPage();
//           }),);
//           debugPrint("You pressed button");
//         },
//         child: const Text('Go see the Planets'),
//       ),

//     );
//   }
// }
