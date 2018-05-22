package com.jpa.entities;

import lombok.Getter;
import lombok.Setter;
import org.apache.johnzon.mapper.JohnzonIgnore;

import javax.persistence.*;
import java.util.ArrayList;
import java.util.List;

@Getter
@Setter
@Entity
@Table(name="BOOK")
public class Book
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="ID")
    private Integer id;

    @Column(name="TITLE")
    private String title;

    @Column(name="DESCRIPTION")
    private String description;

    @JohnzonIgnore
    @JoinColumn(name = "STUDENT_ID", referencedColumnName = "ID")
    @ManyToOne
    private Student student;

    @JohnzonIgnore
    @JoinTable(name = "AUTHOR_BOOK", joinColumns = {
            @JoinColumn(name = "BOOK_ID", referencedColumnName = "ID")}, inverseJoinColumns = {
            @JoinColumn(name = "AUTHOR_ID", referencedColumnName = "ID")})
    @ManyToMany
    private List<Author> authorList = new ArrayList<Author>();

    @Override
    public boolean equals(Object other)
    {
        return (other != null && getClass() == other.getClass() && id != null)
                ? id.equals(((Book) other).id)
                : (other == this);
    }

    @Override
    public int hashCode()
    {
        return (id != null)
                ? (getClass().hashCode() + id.hashCode())
                : super.hashCode();
    }
    @Override
    public String toString()
    {
        return String.format("Book[%d, %s, %s]", id, title, description);
    }
}
