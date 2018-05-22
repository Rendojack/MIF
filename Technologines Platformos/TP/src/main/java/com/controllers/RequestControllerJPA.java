package com.controllers;

import com.business.strategy.IAsyncTask;
import com.business.StringValidator;
import com.business.StudentValidator;
import com.business.decorator.IEncryptor;
import com.jpa.dao.BookDAO;
import com.jpa.dao.StudentDAO;
import com.jpa.entities.Book;
import com.jpa.entities.Student;
import lombok.Getter;
import lombok.Setter;

import javax.annotation.PostConstruct;
import javax.enterprise.inject.Model;
import javax.inject.Inject;
import javax.transaction.Transactional;
import java.util.List;
import java.util.concurrent.Future;

@Model
public class RequestControllerJPA
{
    @Getter
    private Student student = new Student();
    @Getter
    private Book book = new Book();
    @Getter
    private List<Student> allStudents;
    @Getter
    private List<Book> allBooks;
    @Getter
    @Setter
    private Book selectedBook;
    @Getter
    @Setter
    private Student selectedStudent;

    @PostConstruct
    public void init()
    {
        loadAllStudents();
        loadAllBooks();
    }

    @Inject
    private StudentDAO studentDAO;
    @Inject
    private BookDAO bookDAO;
    @Inject
    private StudentValidator studentValidator;
    @Inject
    private StringValidator stringValidator;
    @Inject
    private IAsyncTask asyncTask;
    @Inject
    private IEncryptor encryptor;

    private Future<String> asyncResult = null;

    @Transactional
    public void createStudent()
    {
        try
        {
            if(!studentValidator.isValidName(student.getFirstName()) || !studentValidator.isValidName(student.getLastName()) ||
                    stringValidator.isNullOrWhiteSpace(student.getFirstName()) || stringValidator.isNullOrWhiteSpace(student.getLastName()))
            {
                throw new Exception("Illegal input");
            }
            else
            {
                asyncResult = asyncTask.runAsync();
                if(asyncResult.isDone())
                {
                    System.out.println("AsyncTask result is: " + asyncResult.get());
                }

                student.setLastName(encryptor.encrypt(student.getLastName()));
                studentDAO.create(student);
            }
        }
        catch (Exception e)
        {
            System.out.println("ERROR: " + e.getMessage());
        }
    }

    @Transactional
    public void createBook()
    {
        try
        {
            if(stringValidator.isNullOrWhiteSpace(book.getTitle()) || stringValidator.isNullOrWhiteSpace(book.getDescription()))
            {
                throw new Exception("Illegal input");
            }
            else
            {
                bookDAO.create(book);
            }
        }
        catch (Exception e)
        {
            System.out.println("ERROR: " + e.getMessage());
        }
    }

    private void loadAllStudents()
    {
        allStudents = studentDAO.getAll();
    }
    private void loadAllBooks()
    {
        allBooks = bookDAO.getAll();
    }

    @Transactional
    public void lendBook()
    {
        try
        {
            System.out.println("Student '" + selectedStudent.getFirstName() + " " + selectedStudent.getLastName() + "' is taking book '" + selectedBook.getTitle() + "' out of the library...");
            selectedBook.setStudent(selectedStudent);
            bookDAO.update(selectedBook);
            System.out.println("Success!");
        }
        catch (Exception e)
        {
            System.out.println("ERROR: " + ((e.getMessage()!= null)? e.getMessage():"Illegal selection"));
        }

    }
}