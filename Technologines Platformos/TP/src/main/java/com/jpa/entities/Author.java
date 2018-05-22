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
@Table(name="AUTHOR")
public class Author
{
    @Id
    @GeneratedValue(strategy = GenerationType.IDENTITY)
    @Column(name="ID")
    private Integer id;

    @Column(name="FIRST_NAME")
    private String firstName;

    @Column(name="LAST_NAME")
    private String lastName;

    @JohnzonIgnore
    @JoinTable(name = "AUTHOR_BOOK", joinColumns = {
            @JoinColumn(name = "AUTHOR_ID", referencedColumnName = "ID")}, inverseJoinColumns = {
            @JoinColumn(name = "BOOK_ID", referencedColumnName = "ID")})
    @ManyToMany
    private List<Book> bookList = new ArrayList<Book>();
}
