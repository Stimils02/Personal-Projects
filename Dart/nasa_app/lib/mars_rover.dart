import 'package:flutter/material.dart';
import 'package:nasa_app/favorites_image.dart';
import 'package:nasa_app/api_logic_handler.dart';
import 'package:nasa_app/space_images.dart';
import 'package:provider/provider.dart';
import 'package:nasa_app/data_storage.dart';

class MarsRover extends StatelessWidget {
  final double sol;
  final double numPicture;
  const MarsRover({super.key, this.sol = 0.0, this.numPicture = 0.0});

  Widget _buildPhotoList(BuildContext context, MarsData photo) {
    return ListTile(
        title: Text("${photo.roverName} ${photo.camera}"),
        subtitle: Text(photo.sol.toString()),
        leading: InkWell(
          onTap: () {
            Provider.of<ImageData>(context, listen: false)
                .addImageUrl(photo.url);
            Navigator.of(context).push(
              MaterialPageRoute(
                  builder: (context) => SpaceImages(url: photo.url)),
            );
          },
          child: Image.network(
            photo.url,
            fit: BoxFit.cover,
          ),
        ));
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: const Text("Some Space Images"),
      ),
      body:
          // !Globals.isMarsApiCalled
          // ?
          FutureBuilder<List<MarsData>>(
        future: setMarsItems(numPicture, sol),
        builder: (context, snapshot) {
          debugPrint(snapshot.toString());
          if (snapshot.hasData) {
            List<MarsData> photos = snapshot.data!;
            return ListView.builder(
              itemCount: photos.length,
              itemBuilder: (context, index) {
                return _buildPhotoList(context, photos[index]);
              },
            );
          } else if (snapshot.hasError) {
            return const Center(
              child: Text("Something went wrong"),
            );
          } else {
            return const Center(
              child: CircularProgressIndicator(),
            );
          }
        },
      ),
      // : ListView.builder(
      //     itemCount: Globals.marsDatalist.length,
      //     itemBuilder: (context, index) {
      //       return _buildPhotoList(context, Globals.marsDatalist[index]);
      //     },
      //   ),
    );
  }
}
