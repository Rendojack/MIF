package com.jpa.dao;

import com.jpa.entities.Book;

import javax.enterprise.context.ApplicationScoped;
import javax.inject.Inject;
import javax.persistence.EntityManager;
import java.util.List;

@ApplicationScoped
public class BookDAO
{
    @Inject
    private EntityManager em;

    public void create(Book book)
    {
        em.persist(book);
    }

    public List<Book> getAll()
    {
        return em.createQuery("SELECT b FROM Book b").getResultList();
    }

    public void update(Book book)
    {
        em.merge(book);
    }
}
