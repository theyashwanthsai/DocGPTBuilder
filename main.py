import os

def convert_mdx_to_txt(root_dir, output_file, file_format):
    with open(output_file, 'w', encoding='utf-8') as out_file:
        for subdir, _, files in os.walk(root_dir):
            for file in files:
                if file.endswith(file_format):
                    file_path = os.path.join(subdir, file)
                    with open(file_path, 'r', encoding='utf-8') as mdx_file:
                        content = mdx_file.read()
                        out_file.write(f"{file_path}:\n")
                        out_file.write(f"{content}\n\n")
    print("#### Finshed, check the output file ####")

if __name__ == "__main__":
    print("#### Welcome to docsCustomGPT #####\n")
    root_directory = input("#### Enter the path for the doc repo\n") 
    file_format = input("#### Enter the file format used by your static site (md/mdx)\n")
    output_txt_file = "docs.md"
    convert_mdx_to_txt(root_directory, output_txt_file, file_format)
    
