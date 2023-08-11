import 'package:flutter/material.dart';
import 'package:nasa_app/favorites_image.dart';
import 'package:nasa_app/api_logic_handler.dart';
import 'package:nasa_app/space_images.dart';
import 'package:provider/provider.dart';
import 'package:nasa_app/data_storage.dart';

class APOD extends StatelessWidget {
  final double numPictures;
  const APOD({super.key, this.numPictures = 0.0});

  @override
  Widget build(BuildContext context) {
    return Scaffold(
        appBar: AppBar(
          title: const Text("Some Space Images"),
        ),
        body:
            // !Globals.isApodApiCalled
            //     ?
            FutureBuilder<List<ApodData>>(
          future: setAPODItems(numPictures),
          builder: (context, snapshot) {
            // return Container();
            // // Peek at some other future functions
            // // debugPrint(snapshot.toString());
            if (snapshot.hasData) {
              List<ApodData> image = snapshot.data!;
              return ListView.builder(
                itemCount: image.length,
                itemBuilder: (context, index) {
                  return ListTile(
                      title: Text(image[index].title),
                      subtitle: Text(image[index].date),
                      leading: InkWell(
                        onTap: () {
                          Provider.of<ImageData>(context, listen: false)
                              .addImageUrl(image[index].hdUrl);
                          Navigator.of(context).push(
                            MaterialPageRoute(
                                builder: (context) =>
                                    SpaceImages(url: image[index].hdUrl)),
                          );
                        },
                        child: Image.network(
                          image[index].hdUrl,
                          fit: BoxFit.cover,
                        ),
                      ));
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
        )
        // : ListView.builder(
        //     itemCount: Globals.apodDatalist.length,
        //     itemBuilder: (context, index) {
        //       return ListTile(
        //           title: Text(Globals.apodDatalist[index].title),
        //           subtitle: Text(Globals.apodDatalist[index].date),
        //           leading: InkWell(
        //             onTap: () {
        //               // Add code where images clicked still gets added to favorite Images tab

        //               Navigator.of(context).push(
        //                 MaterialPageRoute(
        //                     builder: (context) => SpaceImages(
        //                         url: Globals.apodDatalist[index].hdUrl)),
        //               );
        //             },
        //             child: Image.network(
        //               Globals.apodDatalist[index].hdUrl,
        //               fit: BoxFit.cover,
        //             ),
        //           ));
        //     },
        //   ),
        );
  }
}






// class APOD extends StatefulWidget {
//   const APOD({super.key});

//   @override
//   State<APOD> createState() => _APODState();
// }

// class _APODState extends State<APOD> {
//   final apiKey = "77D8wvth4JcTKpPrCXBaHlJ2kWGYd6bAnFdb0rpF";
//   final apiUrl = "https://api.nasa.gov/planetary/apod?api_key=";
//   Map<String, dynamic>? images;

//   Future<Map<String, dynamic>> getAPOD() async {
//     final response = await http.get(Uri.parse(apiUrl + apiKey));

//     if (response.statusCode == 200) {
//       print(json.decode(response.body));
//       return json.decode(response.body);
//     } else {
//       throw Exception("Failed to load APOD");
//     }
//   }

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text("APOD Images"),
//       ),
//       body: images == null
//           ? Center(
//               child: ElevatedButton(
//                 onPressed: () async {
//                   final fetchedImages = await getAPOD();
//                   setState(() {
//                     images = fetchedImages;
//                   });
//                 },
//                 child: const Text("Press to get APOD"),
//               ),
//             )
//           : ListView.builder(
//               itemCount: 1,
//               itemBuilder: (context, index) {
//                 final image = images!;
//                 return ListTile(
//                   title: Text(image['title']),
//                   subtitle: Text(image['data']),
//                   leading: Image.network(image['url']),
//                 );
//               },
//             ),
//     );
//   }
// }

// class APOD extends StatelessWidget {
//   const APOD({super.key});

//   @override
//   Widget build(BuildContext context) {
//     return Scaffold(
//       appBar: AppBar(
//         title: const Text("APOD"),
//       ),
//       body: Center(
//         child: ElevatedButton(
//           onPressed: () {
//             getAPOD();
//           },
//           child: const Text("Press this to get APOD"),
//         ),
//       ),
//     );
//   }

//   Future<Map<String, dynamic>> getAPOD() async {
//     String apiKey = "77D8wvth4JcTKpPrCXBaHlJ2kWGYd6bAnFdb0rpF";
//     String url = "https://api.nasa.gov/planetary/apod?api_key=$apiKey";
//     final response = await http.get(Uri.parse(url));

//     if (response.statusCode == 200) {
//       print(json.decode(response.body));
//       return json.decode(response.body);
//     } else {
//       throw Exception("Failed to load APOD");
//     }
//   }

//   // void getAPOD() async {
//   //   String apiKey = "77D8wvth4JcTKpPrCXBaHlJ2kWGYd6bAnFdb0rpF";

//   //   var url = Uri.http("https://api.nasa.gov/planetary/apod?api_key=$apiKey");
//   //   print(url);
//   // }
// }
