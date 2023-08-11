import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:nasa_app/explore_api.dart';
import 'package:nasa_app/home_page.dart';
import 'package:nasa_app/theme_handler.dart';
import 'package:nasa_app/space_images.dart';
import 'package:nasa_app/favorites_image.dart';

class NavigationProvider extends ChangeNotifier {
  int _currentIndex = 0;
  int get currentIndex => _currentIndex;
  void updateIndex(int index) {
    _currentIndex = index;
    notifyListeners();
  }
}

class ControlCenter extends StatelessWidget {
  const ControlCenter({super.key});
  final List<Widget> pages = const [
    HomePage(),
    ExploreAPI(),
    SpaceImages(),
    FavoriteImages(),
  ];
  static const List<BottomNavigationBarItem> navItems = [
    BottomNavigationBarItem(
      icon: Icon(Icons.home_rounded),
      label: "Home",
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.key),
      label: "Explore API",
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.image),
      label: "See Space Images",
    ),
    BottomNavigationBarItem(
      icon: Icon(Icons.favorite),
      label: "Favorites",
    ),
  ];
  @override
  Widget build(BuildContext context) {
    ThemeModel model = Provider.of<ThemeModel>(context);
    return Scaffold(
      body: pages[Provider.of<NavigationProvider>(context).currentIndex],
      bottomNavigationBar: BottomNavigationBar(
        backgroundColor: model.backgroundColor,
        unselectedItemColor: model.textColor,
        selectedItemColor: model.isDarkTheme ? Colors.green : Colors.blue,
        // selectedItemColor: ,
        items: navItems,
        currentIndex: Provider.of<NavigationProvider>(context).currentIndex,
        onTap: (index) {
          Provider.of<NavigationProvider>(context, listen: false)
              .updateIndex(index);
        },
      ),
    );
  }
}
