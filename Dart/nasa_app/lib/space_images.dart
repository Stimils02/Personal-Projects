import 'package:flutter/material.dart';
import 'package:provider/provider.dart';
import 'package:nasa_app/theme_handler.dart';

class SpaceImages extends StatelessWidget {
  final String url;
  const SpaceImages({super.key, this.url = ''});

  @override
  Widget build(BuildContext context) {
    ThemeModel model = Provider.of<ThemeModel>(context);
    bool showImage = url == '' ? false : true;
    return Scaffold(
      appBar: AppBar(
        leading: IconButton(
            onPressed: () => Navigator.pop(context),
            icon: const Icon(Icons.arrow_back)),
      ),
      backgroundColor: model.backgroundColor,
      body: Center(
        child: showImage
            ? Image.network(
                url,
                fit: BoxFit.cover,
              )
            : const Text(
                "No Image Selected Currently",
                style: TextStyle(fontSize: 20),
              ),
      ),
    );
  }
}
