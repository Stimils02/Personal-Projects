import 'package:flutter/material.dart';
import 'package:nasa_app/theme_handler.dart';
import 'package:provider/provider.dart';

class SettingsPage extends StatefulWidget {
  const SettingsPage({super.key});

  @override
  State<SettingsPage> createState() => _SettingsPageState();
}

class _SettingsPageState extends State<SettingsPage> {
  @override
  Widget build(BuildContext context) {
    bool isDarkMode = Provider.of<ThemeModel>(context).isDarkTheme;
    return Scaffold(
      appBar: AppBar(
        title: const Text("Settings"),
      ),
      body: Center(
        child: Column(
          children: [
            const SizedBox(
              height: 24,
            ),
            Text(
              isDarkMode ? 'Dark Mode On' : 'Dark Mode Off',
              style: const TextStyle(fontSize: 20),
            ),
            const SizedBox(),
            Switch(
                value:
                    Provider.of<ThemeModel>(context).isDarkTheme ? true : false,
                onChanged: (newvalue) {
                  Provider.of<ThemeModel>(context, listen: false).switchMode();
                  // setState(() {
                  //   isDarkMode = newvalue;
                  // });
                })
          ],
        ),
      ),
    );
  }
}

// class SettingsPage extends StatelessWidget {
//   const SettingsPage({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//         backgroundColor: Colors.black,
//         appBar: AppBar(
//           title: const Text("Settings"),
//         ),
//         body: Theme(
//           data: Theme.of(context).copyWith(scaffoldBackgroundColor: Colors.red),
//           child: const Center(
//             child: Text("This is the Settings Page"),
//           ),
//         ));
//   }
// }



// // This NasaApp widget is gonna manage its own state
// class NasaApp extends StatefulWidget {
//   const NasaApp({super.key});

//   @override
//   State<NasaApp> createState() => NasaAppState();
// }

// class NasaAppState extends State<NasaApp> {
//   bool isDarkTheme = false;

//   @override
//   Widget build(BuildContext context) {
//     return MaterialApp(
//       theme: isDarkTheme ? darkTheme : lightTheme,
//       darkTheme: ThemeData(
//         primarySwatch: Colors.amber,
//         brightness: Brightness.dark,
//       ),
//       home: Scaffold(
//         body: const RootPage(),
//         appBar: AppBar(title: const Text('Nasa App'), actions: [
//           IconButton(
//             onPressed: () {
//               setState(() {
//                 isDarkTheme = !isDarkTheme;
//               });
//             },
//             icon: Icon(isDarkTheme ? iconDark : iconLight),
//           ),
//         ]),
//       ),
//       debugShowCheckedModeBanner: false,
//     );
//   }
// }
