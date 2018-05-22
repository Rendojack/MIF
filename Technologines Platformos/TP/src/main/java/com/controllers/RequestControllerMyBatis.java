package com.controllers;

import com.business.StringValidator;
import com.business.StudentValidator;
import com.mybatis.dao.StudentMapper;
import com.mybatis.dao.BookMapper;
import com.mybatis.model.Student;
import com.mybatis.model.Book;
import lombok.Getter;
import lombok.Setter;
import javax.annotation.PostConstruct;
import javax.enterprise.inject.Model;
import javax.inject.Inject;
import javax.transaction.Transactional;
import java.util.List;

@Model
public class RequestControllerMyBatis
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
    private StudentMapper studentMapper;
    @Inject
    private BookMapper bookMapper;
    @Inject
    private StudentValidator studentValidator;
    @Inject
    private StringValidator stringValidator;

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
                studentMapper.insert(student);
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
                throw new Exception("Illegal input");
            else
            {
                bookMapper.insert(book);
            }
        }
        catch (Exception e)
        {
            System.out.println("ERROR: " + e.getMessage());
        }
    }
    @Transactional
    public void lendBook()
    {
        try
        {
            System.out.println("Student '" + selectedStudent.getFirstName() + " " + selectedStudent.getLastName() + "' is taking book '" + selectedBook.getTitle() + "' out of the library...");
            selectedBook.setStudentId(selectedStudent.getId());
            selectedBook.setStudent(selectedStudent);
            bookMapper.update(selectedBook);
            System.out.println("Success!");
        }
        catch (Exception e)
        {
            System.out.println("ERROR: " + ((e.getMessage()!= null)? e.getMessage():"Illegal selection"));
        }
    }

    private void loadAllStudents()
    {
        allStudents = studentMapper.selectAll();
    }

    private void loadAllBooks()
    {
        allBooks = bookMapper.selectAll();
    }
}
