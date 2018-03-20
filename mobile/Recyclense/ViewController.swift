//
//  ViewController.swift
//  Recyclense
//
//  Created by Scott Fitsimones on 9/30/17.
//  Copyright © 2017 Recyclense, Inc. All rights reserved.
//

import UIKit


class ViewController: UIViewController, UIImagePickerControllerDelegate, UINavigationControllerDelegate {

    @IBOutlet var imageView: UIImageView!
    
    @IBOutlet var statusEmoji: UILabel!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        statusEmoji.backgroundColor = UIColor(displayP3Red: 0.9, green: 0.9, blue: 0.9, alpha: 0.7)
        let pop = UITapGestureRecognizer(target: self, action: #selector(self.takePhoto))
        imageView.contentMode = .scaleAspectFill
        imageView.isUserInteractionEnabled = true
        imageView.addGestureRecognizer(pop)
        // Do any additional setup after loading the view, typically from a nib.
    }
    
    @objc func takePhoto() {
        print("here")
        
        let imagePicker = UIImagePickerController()
        imagePicker.sourceType = .camera
        imagePicker.delegate = self
        self.present(imagePicker, animated: true) {}
    }
     func imagePickerController(_ picker: UIImagePickerController, didFinishPickingMediaWithInfo info: [String : Any]) {
        // Media
        self.dismiss(animated: false, completion: nil)
        self.imageView.image = info[UIImagePickerControllerOriginalImage] as? UIImage
        uploadImageToGoogleCloud(image: info[UIImagePickerControllerOriginalImage] as! UIImage, completion: {success, string -> Void in
                print(string)
            self.checkImage()
        });
    }
    func checkImage() {
        let url = URL(string: "http://35.185.205.9/classify")
        var request = URLRequest(url: url!)
        request.httpMethod = "GET"
        let session = URLSession.shared
        print("Here")
        session.dataTask(with: request, completionHandler: { (data, response, error) in
            // do stuff with response, data & error here
            let responseString = NSString(data: data!, encoding: String.Encoding.utf8.rawValue)
            print(responseString!)
            DispatchQueue.main.async {
            self.statusEmoji.text! = responseString! as String
            }
            }).resume()
    }
    func uploadImageToGoogleCloud(image: UIImage, completion:@escaping (_ error: Bool, _ details: String) -> Void) {
        let uploadUrl = "http://storage.googleapis.com/recycleanse/image.png"
        let imageData = UIImageJPEGRepresentation(image, 100)
        
        let request = NSMutableURLRequest(url:NSURL(string:uploadUrl)! as URL);
        request.httpMethod = "PUT"
        request.addValue("image/jpeg", forHTTPHeaderField: "Content-Type")
//        request.addValue("public-read-write", forHTTPHeaderField: "Content-Type")
        
        let uploadSession = URLSession.shared
        let data = Data(imageData!)
        request.httpBody = data
    
    // The upload task using NSURLSession
        var uploadTask = uploadSession.uploadTask(with: request as! URLRequest, from:data,
    completionHandler: { data, response, error -> Void in
        print(response!)
    if error == nil {
        var httpResponse = response as? HTTPURLResponse
        var statusCode = httpResponse!.statusCode;
    if statusCode == 200 || statusCode == 201 {
        completion(false, "");
    } else {
    var responseString = NSString(data: data!, encoding: String.Encoding.utf8.rawValue)
    print(responseString)
    completion (true, String(format: "Code: %@, Headers: %@", statusCode,
    httpResponse!.allHeaderFields ))
    }
    } else {
    
    }
    })
    uploadTask.resume()
    }
    
    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    
    

}

