#include "itkImage.h"
#include "itkGrayscaleDilateImageFilter.h"
#include "itkImageFileReader.h"
#include "itkBinaryCrossStructuringElement.h"
#include "itkSubtractImageFilter.h"
#include "itkImageFileWriter.h"

int main(int argc, char *argv[])
{
    std::cout << "YO" << std::endl;
    /*if(argc < 2)
    {
    std::cerr << "Usage: " << std::endl;
    std::cerr << argv[0] << " InputImageFile [radius]" << std::endl;
    return EXIT_FAILURE;
    }

  unsigned int radius = 2;
  if (argc > 2)
    {
    radius = atoi(argv[2]);
    }

  std::string inputFilename = argv[1];

  typedef itk::Image<unsigned char, 2>    ImageType;
  typedef itk::ImageFileReader<ImageType> ReaderType;
  //ReaderType::Pointer reader = ReaderType::New();
  //reader->SetFileName(inputFilename);

  typedef itk::BinaryCrossStructuringElement<
    ImageType::PixelType,2> StructuringElementType;
  StructuringElementType structuringElement;
  structuringElement.SetRadius(radius);
  structuringElement.CreateStructuringElement();

  typedef itk::GrayscaleDilateImageFilter <ImageType, ImageType, StructuringElementType>
    GrayscaleDilateImageFilterType;

  GrayscaleDilateImageFilterType::Pointer dilateFilter
    = GrayscaleDilateImageFilterType::New();
  dilateFilter->SetInput(reader->GetOutput());
  dilateFilter->SetKernel(structuringElement);

  typedef itk::ImageFileWriter<ImageType> WriterType;
  WriterType::Pointer writer = WriterType::New();
  writer->SetFileName( "output.png" );
  writer->SetInput(dilateFilter->GetOutput());
  writer->Update();*/

  return EXIT_SUCCESS;
}
