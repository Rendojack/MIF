package com.rest;

import com.jpa.entities.Student;
import org.apache.deltaspike.core.api.message.Message;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.persistence.EntityManager;
import javax.transaction.Transactional;
import javax.ws.rs.*;
import javax.ws.rs.core.MediaType;
import javax.ws.rs.core.Response;

@ApplicationScoped
@Path("/student")
public class StudentRestService
{
    @Inject
    private EntityManager em;

    @Path("/hello")
    @GET
    @Produces({MediaType.TEXT_PLAIN})
    public String message()
    {
        return "Hello!";
    }

    @Path("/{id}")
    @GET
    @Produces({MediaType.APPLICATION_JSON})
    public Student getStudent(@PathParam("id") Integer id)
    {
        return em.find(Student.class, id);
    }

    @Path("/create")
    @POST
    @Transactional
    @Consumes("application/json")
    public Student createStudent(Student student)
    {
        em.persist(student);
        return student;
    }

    @Path("/update/{id}")
    @PUT
    @Transactional
    @Consumes("application/json")
    public Response updateStudent(Student student, @PathParam("id") Integer id)
    {
        Student studentToUpdate = em.find(Student.class, id);
        if(studentToUpdate == null)
        {
            throw new IllegalArgumentException("User not found");
        }
        studentToUpdate.setFirstName(student.getFirstName());
        studentToUpdate.setLastName(student.getLastName());

        em.merge(studentToUpdate);
        return Response.ok(studentToUpdate).build();
    }
}
