import 'package:flutter/material.dart';
import 'package:nasa_app/api_logic_handler.dart';
import 'package:nasa_app/theme_handler.dart';
import 'package:provider/provider.dart';

class AboutPage extends StatelessWidget {
  const AboutPage({super.key});

  @override
  Widget build(BuildContext context) {
    ThemeModel model = Provider.of<ThemeModel>(context);
    return Scaffold(
        appBar: AppBar(
          title: const Text("This is the About Page"),
        ),
        body: Column(
          children: [
            Padding(
              padding: const EdgeInsets.all(16.0),
              child: Text(
                "The NASA App is a mobile application that allows users to explore and learn about space, including features such as Astronomy Picture of the Day (APOD) and the Mars Rover Photos API. The APOD feature presents a new astronomical image or photograph each day with a brief explanation by a professional astronomer. The Mars Rover Photos API provides access to images taken by the Mars rovers, allowing users to see the Martian landscape and learn about the latest discoveries made by NASA on the red planet. The app provides a wealth of information and opportunities to learn about space exploration and the latest scientific discoveries from NASA.",
                style: TextStyle(fontSize: 20, color: model.textColor),
              ),
            ),
            ElevatedButton(
              onPressed: () {
                getAPOD(5);
              },
              child: const Text("Invoke Mars API"),
            ),
          ],
        ));
  }
}
