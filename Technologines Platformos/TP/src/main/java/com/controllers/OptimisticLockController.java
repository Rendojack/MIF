package com.controllers;

import com.logging.Log;
import lombok.Getter;
import lombok.extern.slf4j.Slf4j;
import org.hibernate.Hibernate;
import org.omnifaces.cdi.ViewScoped;
import org.primefaces.PrimeFaces;
import org.primefaces.context.RequestContext;

import javax.annotation.PostConstruct;
import javax.inject.Inject;
import javax.inject.Named;
import javax.persistence.OptimisticLockException;
import javax.transaction.Transactional;

import com.jpa.dao.StudentDAO;
import com.jpa.entities.Student;

import java.io.Serializable;
import java.util.List;

@Named
@ViewScoped
public class OptimisticLockController implements Serializable
{

    @Getter private Student selectedStudent;
    @Getter private Student conflictingStudent;
    @Getter private List<Student> allStudents;

    @Inject private StudentDAO studentDAO;


    @PostConstruct
    public void init() {
        reloadAll();
    }

    public void prepareForEditing(Student student)
    {
        selectedStudent = student;
        conflictingStudent = null;
    }

    @Transactional
    @Log
    public void updateSelectedStudent()
    {
        try
        {
            studentDAO.update(selectedStudent);
            reloadAll();
        }
        catch (OptimisticLockException ole)
        {
            conflictingStudent = studentDAO.getStudentById(selectedStudent.getId());
            PrimeFaces.current().ajax().addCallbackParam("validationFailed", true);
        }
    }

    @Transactional
    public void overwriteStudent()
    {
        selectedStudent.setRowVersion(conflictingStudent.getRowVersion());
        updateSelectedStudent();
    }

    public void reloadAll()
    {
        allStudents = studentDAO.getAll();
    }
}
