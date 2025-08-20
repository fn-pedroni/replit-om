# PDF Text Extractor

## Overview

A lightweight, stateless Flask web application with plain HTML/CSS for PDF upload and immediate text extraction. The application provides a clean, user-friendly interface for PDF text extraction using PyPDF2 library, with support for drag-and-drop file uploads and real-time text display.

## User Preferences

Preferred communication style: Simple, everyday language.

## System Architecture

### Frontend Architecture
- **Template Engine**: Jinja2 templates with Flask's built-in rendering
- **Styling**: Bootstrap with Replit's dark theme CSS for consistent styling
- **User Interface**: Single-page application with drag-and-drop file upload area
- **File Handling**: Client-side file validation and upload progress feedback
- **JavaScript**: Vanilla JavaScript for drag-and-drop functionality and clipboard operations

### Backend Architecture
- **Web Framework**: Flask with minimal configuration for lightweight operation
- **File Processing**: PyPDF2 library for PDF text extraction
- **Request Handling**: Simple POST/GET route structure with form-based file uploads
- **Error Handling**: Basic exception handling with user-friendly error messages
- **Security**: File type validation and size limits (16MB max)
- **File Storage**: Temporary in-memory processing (files not persisted to disk)

### Data Storage
- **Session Management**: Flask sessions with configurable secret key
- **File Storage**: Temporary in-memory processing (files not persisted to disk)
- **Text Processing**: Real-time extraction and display without permanent storage
- **Database**: None - completely stateless application

### Configuration Management
- **Environment Variables**: Support for SESSION_SECRET configuration
- **File Restrictions**: Configurable file size limits and allowed extensions
- **Logging**: Built-in Python logging with debug level support

## External Dependencies

### Core Libraries
- **Flask**: Web framework for handling HTTP requests and rendering templates
- **PyPDF2**: PDF parsing and text extraction functionality
- **Werkzeug**: Secure filename handling and utilities

### Frontend Assets
- **Bootstrap CDN**: UI framework loaded from Replit's CDN for consistent styling
- **Custom CSS**: Dark theme support and responsive design enhancements

### Runtime Environment
- **Python**: Server-side application runtime
- **Development Server**: Flask's built-in development server for local testing