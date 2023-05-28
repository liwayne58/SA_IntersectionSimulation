import os


def run(path):
    for doc in os.listdir(path):
        docPath = os.path.join(path, doc)
        if os.path.isdir(doc):
            for sDoc in os.listdir(doc):
                sDocPath = os.path.join(docPath, sDoc)
                if not os.path.isdir(sDoc):
                    renamePath = os.path.join(docPath, sDoc.upper())
                    # print(renamePath)
                    os.rename(sDocPath, sDocPath.upper())


if __name__ == '__main__':
    run(r"D:\PythonProjects\SA_IntersectionSimulation\Data\Images")
