/**
 * @license Copyright (c) 2003-2022, CKSource Holding sp. z o.o. All rights reserved.
 * For licensing, see https://ckeditor.com/legal/ckeditor-oss-license
 */

CKEDITOR.editorConfig = function( config ){
    config.language = 'en';
    config.uiColor = '#ffffff';
    config.filebrowserUploadMethod = 'form';
    config.extraPlugins = 'filebrowser';
    config.filebrowserBrowseUrl = '/browser/browse.php';
    config.filebrowserUploadUrl = '/uploader/upload.php';

	// Define changes to default configuration here. For example:
	// config.language = 'fr';
	// config.uiColor = '#AADC6E';
};
