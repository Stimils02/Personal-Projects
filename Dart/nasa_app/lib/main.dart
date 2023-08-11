import 'package:flutter/material.dart';
import 'package:nasa_app/nav_controller.dart';
import 'package:provider/provider.dart';
import 'package:nasa_app/favorites_image.dart';
import 'package:nasa_app/theme_handler.dart';
import 'package:nasa_app/apod_select_page.dart';

// CurrentlySelected Image Provider
// On that Selected Image page add to list of favorites provider
void main() {
  runApp(
    MultiProvider(
      providers: [
        ChangeNotifierProvider(
          create: (_) => NavigationProvider(),
        ),
        ChangeNotifierProvider(
          create: (_) => ImageData(),
        ),
        ChangeNotifierProvider(
          create: (_) => ThemeModel(),
        ),
        ChangeNotifierProvider(
          create: (_) => ApodProvider(),
        ),
      ],
      child: const NasaApp(),
    ),
  );
}

class NasaApp extends StatelessWidget {
  const NasaApp({super.key});

  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: Provider.of<ThemeModel>(context).currentTheme,
      title: "Nasa App",
      home: Consumer<NavigationProvider>(
        builder: (context, provider, child) => const ControlCenter(),
      ),
      debugShowCheckedModeBanner: false,
    );
  }
}



















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

// class RootPage extends StatefulWidget {
//   const RootPage({super.key});

//   @override
//   State<RootPage> createState() => RootPageState();
// }

// class RootPageState extends State<RootPage> {
//   int currentPage = 0;

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       body: const HomePage(),
//       floatingActionButton: Theme(
//         data: Theme.of(context),
//         child: FloatingActionButton(
//           onPressed: () {
//             debugPrint("You Pressed on home!");
//           },
//           child: const Icon(Icons.home),
//         ),
//       ),
//       bottomNavigationBar: NavigationBar(
//         destinations: const [
//           NavigationDestination(icon: Icon(Icons.home), label: 'Home'),
//           NavigationDestination(icon: Icon(Icons.star), label: 'Space Images'),
//           NavigationDestination(icon: Icon(Icons.person), label: 'Profile'),
//         ],
//         onDestinationSelected: (int index) {
//           setState(() {
//             currentPage = index;
//           });
//         },
//         selectedIndex: currentPage,
//       ),
//     );
//   }
// }
