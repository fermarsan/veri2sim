module example (input a, output b);
    wire w;
    assign w = ~a;
    assign b = w;
endmodule

