package com.jpa.dao;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.persistence.EntityManager;
import java.util.List;
import java.util.concurrent.ExecutionException;
import java.util.concurrent.Future;

import com.business.strategy.IAsyncTask;
import com.jpa.entities.Student;

@ApplicationScoped
public class StudentDAO
{
    @Inject
    private EntityManager em;

    public void create(Student student)
    {
        em.persist(student);
    }

    public void update(Student student)
    {
        em.merge(student);
        em.flush();
    }

    public Student getStudentById(Integer id)
    {
        return em.find(Student.class, id);
    }

    public List<Student> getAll()
    {
        return em.createQuery("SELECT s FROM Student s").getResultList();
    }
}
