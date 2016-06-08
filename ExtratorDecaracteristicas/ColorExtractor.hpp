//
//  ColorExtractor.hpp
//  ExtratorDeCaracteristicas
//
//  Created by joao lopes on 08/06/16.
//
//

#ifndef ColorExtractor_hpp
#define ColorExtractor_hpp

#include <stdio.h>
#include "itkImage.h"
#include "itkImageFileReader.h"
#include "itkImageFileWriter.h"
#include "itkRGBToLuminanceImageFilter.h"

using namespace std;
using namespace itk;

const int DIMENSIONS = 2;

typedef Image<unsigned char , DIMENSIONS> GrayscaleImageType;
typedef RGBPixel<unsigned char> RGBPixelType;
typedef Image<RGBPixelType , DIMENSIONS> RGBImageType;
typedef ImageFileReader<RGBImageType> RGBReaderType;
typedef RGBToLuminanceImageFilter<RGBImageType, GrayscaleImageType> GrayscaleFilterType;

class ColorExtractor{
private:
    RGBImageType::Pointer image;
    int bartShirt;
    int bartShortsAndShoes;
    int homerBeard;
    int homerPants;
    int lisaDressAndMaggiePacifierAndMargeItems;
    int maggiePijamas;
    int margeHair;
    int margeDress;
    void GetData();
public:
    ColorExtractor(RGBImageType::Pointer image);
    void GetValues(int* vetResults);
};

#endif /* ColorExtractor_hpp */
