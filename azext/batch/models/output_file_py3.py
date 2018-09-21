# --------------------------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# --------------------------------------------------------------------------------------------

from msrest.serialization import Model


class OutputFile(Model):
    """A specification for uploading files from an Azure Batch node to another
    location after the Batch service has finished executing the task process.

    :param file_pattern: A pattern indicating which file(s) to upload. Both
     relative and absolute paths are supported. Relative paths are relative to
     the task working directory. The following wildcards are supported: *
     matches 0 or more characters (for example pattern abc* would match abc or
     abcdef), ** matches any directory, ? matches any single character, [abc]
     matches one character in the brackets, and [a-c] matches one character in
     the range. Brackets can include a negation to match any character not
     specified (for example [!abc] matches any character but a, b, or c). If a
     file name starts with "." it is ignored by default but may be matched by
     specifying it explicitly (for example *.gif will not match .a.gif, but
     .*.gif will). A simple example: **\\*.txt matches any file that does not
     start in '.' and ends with .txt in the task working directory or any
     subdirectory. If the filename contains a wildcard character it can be
     escaped using brackets (for example abc[*] would match a file named abc*).
     Note that both \\ and / are treated as directory separators on Windows,
     but only / is on Linux. Environment variables (%var% on Windows or $var on
     Linux) are expanded prior to the pattern being applied.
    :type file_pattern: str
    :param destination: The destination for the output file(s).
    :type destination: :class:`ExtendedOutputFileDestination
     <azext.batch.models.ExtendedOutputFileDestination>`
    :param upload_options: Additional options for the upload operation,
     including under what conditions to perform the upload.
    :type upload_options: :class:`OutputFileUploadOptions
     <azure.batch.models.OutputFileUploadOptions>`
    """

    _validation = {
        'file_pattern': {'required': True},
        'destination': {'required': True},
        'upload_options': {'required': True},
    }

    _attribute_map = {
        'file_pattern': {'key': 'filePattern', 'type': 'str'},
        'destination': {'key': 'destination', 'type': 'ExtendedOutputFileDestination'},
        'upload_options': {'key': 'uploadOptions', 'type': 'OutputFileUploadOptions'},
    }

    def __init__(self, *, file_pattern: str, destination, upload_options, **kwargs) -> None:
        super(OutputFile, self).__init__(**kwargs)
        self.file_pattern = file_pattern
        self.destination = destination
        self.upload_options = upload_options