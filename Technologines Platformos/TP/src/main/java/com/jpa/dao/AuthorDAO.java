package com.jpa.dao;

import com.jpa.entities.Author;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.persistence.EntityManager;
import java.util.List;

@ApplicationScoped
public class AuthorDAO
{
    @Inject
    private EntityManager em;

    public void create(Author author)
    {
        em.persist(author);
    }

    public List<Author> getAll()
    {
        return em.createQuery("SELECT a FROM Author a").getResultList();
    }
}
